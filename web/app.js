let allCards = [];
let filtered = [];
let index = 0;
let flipped = false;

const elDomain = document.getElementById("filter-domain");
const elScenario = document.getElementById("filter-scenario");
const elTask = document.getElementById("filter-task");
const elCounter = document.getElementById("counter");
const elMeta = document.getElementById("card-meta");
const elFront = document.getElementById("card-front");
const elBack = document.getElementById("card-back");
const elCard = document.getElementById("card");

const SCENARIO_ORDER = [
  "customer_support",
  "code_generation",
  "multi_agent_research",
  "developer_productivity",
  "ci_cd",
  "structured_extraction",
];

const SCENARIO_LABELS = {
  customer_support: "Customer Support",
  code_generation: "Code Generation",
  multi_agent_research: "Multi-Agent Research",
  developer_productivity: "Developer Productivity",
  ci_cd: "CI/CD",
  structured_extraction: "Structured Extraction",
};

function sortTasks(tasks) {
  return [...tasks].sort((a, b) => {
    const parse = (x) => {
      if (/^[1-5]\.\d$/.test(x)) {
        const [d, t] = x.split(".").map(Number);
        return [0, d, t];
      }
      return [1, 0, x];
    };
    const pa = parse(a);
    const pb = parse(b);
    return (
      pa[0] - pb[0] ||
      pa[1] - pb[1] ||
      pa[2] - pb[2] ||
      String(a).localeCompare(String(b))
    );
  });
}

function cardsMatchingDomain(domain) {
  if (!domain) return allCards;
  return allCards.filter((c) => c.domain === domain);
}

function cardMatchesScenario(card, scenario) {
  if (!scenario) return true;
  const scenarios = card.scenarios || [];
  return scenarios.includes(scenario) || scenarios.includes("all");
}

function cardsMatchingDomainAndScenario(domain, scenario) {
  return cardsMatchingDomain(domain).filter((c) => cardMatchesScenario(c, scenario));
}

function scenariosForDomain(domain) {
  const cards = cardsMatchingDomain(domain);
  const scenarioSet = new Set();
  let includesAll = false;

  for (const card of cards) {
    const scenarios = card.scenarios || [];
    if (scenarios.includes("all")) {
      includesAll = true;
    }
    for (const s of scenarios) {
      if (s !== "all") scenarioSet.add(s);
    }
  }

  if (includesAll) {
    for (const s of SCENARIO_ORDER) scenarioSet.add(s);
  }

  return SCENARIO_ORDER.filter((s) => scenarioSet.has(s));
}

function tasksForDomainAndScenario(domain, scenario) {
  const cards = cardsMatchingDomainAndScenario(domain, scenario);
  const tasks = new Set();
  for (const card of cards) {
    for (const t of card.tasks || []) tasks.add(t);
  }
  return sortTasks([...tasks]);
}

function setSelectOptions(select, values, labelFn, preserveValue) {
  const wanted = preserveValue || select.value;
  select.replaceChildren();

  const allOpt = document.createElement("option");
  allOpt.value = "";
  allOpt.textContent = "All";
  select.appendChild(allOpt);

  for (const value of values) {
    const opt = document.createElement("option");
    opt.value = value;
    opt.textContent = labelFn(value);
    select.appendChild(opt);
  }

  select.value = values.includes(wanted) ? wanted : "";
}

function updateScenarioOptions() {
  const domain = elDomain.value;
  const scenarios = scenariosForDomain(domain);
  setSelectOptions(
    elScenario,
    scenarios,
    (s) => SCENARIO_LABELS[s] || s,
    elScenario.value
  );
}

function updateTaskOptions() {
  const domain = elDomain.value;
  const scenario = elScenario.value;
  const tasks = tasksForDomainAndScenario(domain, scenario);
  setSelectOptions(elTask, tasks, (t) => t, elTask.value);
}

function applyFilters() {
  const domain = elDomain.value;
  const scenario = elScenario.value;
  const task = elTask.value;

  filtered = allCards.filter((c) => {
    if (domain && c.domain !== domain) return false;
    if (!cardMatchesScenario(c, scenario)) return false;
    if (task) {
      const tasks = c.tasks || [];
      if (!tasks.includes(task)) return false;
    }
    return true;
  });

  if (scenario) {
    filtered.sort((a, b) => {
      const sa = a.chain?.step ?? 999;
      const sb = b.chain?.step ?? 999;
      if (sa !== sb) return sa - sb;
      return a.id.localeCompare(b.id);
    });
  }

  index = 0;
  flipped = false;
  render();
}

function onDomainChange() {
  updateScenarioOptions();
  updateTaskOptions();
  applyFilters();
}

function onScenarioChange() {
  updateTaskOptions();
  applyFilters();
}

function render() {
  if (filtered.length === 0) {
    elCounter.textContent = "No cards match filters";
    elMeta.textContent = "";
    elFront.textContent = "Adjust filters or add cards in YAML.";
    elBack.classList.add("hidden");
    return;
  }

  const card = filtered[index];
  elCounter.textContent = `${index + 1} / ${filtered.length}`;
  const tasks = (card.tasks || []).join(", ");
  const chain = card.chain
    ? ` · chain ${card.chain.step}/${card.chain.steps}`
    : "";
  elMeta.textContent = `${card.id} · ${card.domain} · ${card.type}${chain} · tasks: ${tasks} · ${(card.scenarios || []).join(", ")}`;
  elFront.textContent = card.front;
  elBack.innerHTML =
    `<strong>A:</strong> ${card.back}` +
    (card.rationale ? `<br><br><strong>Why:</strong> ${card.rationale}` : "");
  elBack.classList.toggle("hidden", !flipped);
}

function flip() {
  if (filtered.length === 0) return;
  flipped = !flipped;
  elBack.classList.toggle("hidden", !flipped);
}

function next() {
  if (filtered.length === 0) return;
  index = (index + 1) % filtered.length;
  flipped = false;
  render();
}

function prev() {
  if (filtered.length === 0) return;
  index = (index - 1 + filtered.length) % filtered.length;
  flipped = false;
  render();
}

function shuffle() {
  for (let i = filtered.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [filtered[i], filtered[j]] = [filtered[j], filtered[i]];
  }
  index = 0;
  flipped = false;
  render();
}

function initFiltersFromUrl() {
  const params = new URLSearchParams(window.location.search);
  const domain = params.get("domain");
  const scenario = params.get("scenario");
  const task = params.get("task");

  if (domain) elDomain.value = domain;

  updateScenarioOptions();
  if (scenario && [...elScenario.options].some((o) => o.value === scenario)) {
    elScenario.value = scenario;
  }

  updateTaskOptions();
  if (task && [...elTask.options].some((o) => o.value === task)) {
    elTask.value = task;
  }
}

document.getElementById("flip-btn").addEventListener("click", flip);
document.getElementById("next-btn").addEventListener("click", next);
document.getElementById("prev-btn").addEventListener("click", prev);
document.getElementById("shuffle-btn").addEventListener("click", shuffle);
elDomain.addEventListener("change", onDomainChange);
elScenario.addEventListener("change", onScenarioChange);
elTask.addEventListener("change", applyFilters);
elCard.addEventListener("click", flip);

document.addEventListener("keydown", (e) => {
  if (e.key === " " || e.key === "Enter") {
    e.preventDefault();
    flip();
  } else if (e.key === "ArrowRight") {
    next();
  } else if (e.key === "ArrowLeft") {
    prev();
  }
});

fetch("cards.json")
  .then((r) => r.json())
  .then((data) => {
    allCards = data.cards || [];
    initFiltersFromUrl();
    applyFilters();
  })
  .catch((err) => {
    elFront.textContent = "Failed to load cards.json. Run scripts/build_json.py first.";
    console.error(err);
  });
