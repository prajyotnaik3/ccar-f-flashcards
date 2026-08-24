let allCards = [];
let filtered = [];
let index = 0;
let flipped = false;
let cardsReady = false;

const elKind = document.getElementById("filter-kind");
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

function setFiltersEnabled(enabled) {
  elKind.disabled = !enabled;
  elDomain.disabled = !enabled;
  elScenario.disabled = !enabled;
  elTask.disabled = !enabled;
}

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

function cardScenarios(card) {
  const scenarios = [...(card.scenarios || [])];
  const chainScenario = card.chain?.scenario;
  if (chainScenario && !scenarios.includes(chainScenario)) {
    scenarios.push(chainScenario);
  }
  return scenarios;
}

function cardsMatchingDomain(domain) {
  return cardsForKind().filter((c) => !domain || c.domain === domain);
}

function cardsForKind() {
  const kind = elKind.value;
  if (kind === "notes") {
    return allCards.filter((c) => c.type === "task_notes");
  }
  return allCards.filter((c) => c.type !== "task_notes");
}

function cardMatchesScenario(card, scenario) {
  if (!scenario) return true;
  const scenarios = cardScenarios(card);
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
    const scenarios = cardScenarios(card);
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
  const wanted = preserveValue ?? select.value;
  while (select.firstChild) {
    select.removeChild(select.firstChild);
  }

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

function refreshFilterOptions() {
  updateScenarioOptions();
  updateTaskOptions();
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
  if (!cardsReady) return;

  const domain = elDomain.value;
  const scenario = elScenario.value;
  const task = elTask.value;

  filtered = cardsForKind().filter((c) => {
    if (domain && c.domain !== domain) return false;
    if (!cardMatchesScenario(c, scenario)) return false;
    if (task) {
      const tasks = c.tasks || [];
      if (!tasks.includes(task)) return false;
    }
    return true;
  });

  if (elKind.value === "notes") {
    filtered.sort((a, b) => {
      const ta = (a.tasks || [])[0] || a.id;
      const tb = (b.tasks || [])[0] || b.id;
      return String(ta).localeCompare(String(tb), undefined, { numeric: true });
    });
  } else if (scenario) {
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
  if (!cardsReady) return;
  refreshFilterOptions();
  applyFilters();
}

function onScenarioChange() {
  if (!cardsReady) return;
  updateTaskOptions();
  applyFilters();
}

function escapeHtml(text) {
  return String(text)
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;");
}

function render() {
  if (!cardsReady) {
    elCounter.textContent = "Loading cards…";
    elMeta.textContent = "";
    elFront.textContent = "Loading flashcard deck…";
    elBack.classList.add("hidden");
    return;
  }

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
  elMeta.textContent = `${card.id} · ${card.domain} · ${card.type}${chain} · tasks: ${tasks} · ${cardScenarios(card).join(", ")}`;
  elFront.textContent = card.front;
  const notes = card.notes || [];
  let backHtml = `<strong>${elKind.value === "notes" ? "Notes" : "A"}:</strong> `;
  if (notes.length) {
    backHtml += `<ul class="notes-list">${notes
      .map((n) => `<li>${escapeHtml(n)}</li>`)
      .join("")}</ul>`;
  } else {
    backHtml += escapeHtml(card.back);
  }
  if (card.rationale) {
    backHtml += `<br><br><strong>Why:</strong> ${escapeHtml(card.rationale)}`;
  }
  elBack.innerHTML = backHtml;
  elBack.classList.toggle("hidden", !flipped);
}

function flip() {
  if (!cardsReady || filtered.length === 0) return;
  flipped = !flipped;
  elBack.classList.toggle("hidden", !flipped);
}

function next() {
  if (!cardsReady || filtered.length === 0) return;
  index = (index + 1) % filtered.length;
  flipped = false;
  render();
}

function prev() {
  if (!cardsReady || filtered.length === 0) return;
  index = (index - 1 + filtered.length) % filtered.length;
  flipped = false;
  render();
}

function shuffle() {
  if (!cardsReady || filtered.length === 0) return;
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
  const kind = params.get("kind");
  const domain = params.get("domain");
  const scenario = params.get("scenario");
  const task = params.get("task");

  if (kind === "notes" || kind === "recall") elKind.value = kind;

  if (domain) elDomain.value = domain;

  refreshFilterOptions();

  if (scenario && [...elScenario.options].some((o) => o.value === scenario)) {
    elScenario.value = scenario;
  }

  updateTaskOptions();

  if (task && [...elTask.options].some((o) => o.value === task)) {
    elTask.value = task;
  }
}

function onCardsLoaded(data) {
  allCards = data.cards || [];
  if (allCards.length === 0) {
    elCounter.textContent = "No cards in deck";
    elFront.textContent = "cards.json is empty. Run scripts/build_json.py.";
    return;
  }

  cardsReady = true;
  setFiltersEnabled(true);
  initFiltersFromUrl();
  applyFilters();
}

document.getElementById("flip-btn").addEventListener("click", flip);
document.getElementById("next-btn").addEventListener("click", next);
document.getElementById("prev-btn").addEventListener("click", prev);
document.getElementById("shuffle-btn").addEventListener("click", shuffle);
elKind.addEventListener("change", onDomainChange);
elDomain.addEventListener("change", onDomainChange);
elScenario.addEventListener("change", onScenarioChange);
elTask.addEventListener("change", applyFilters);
elCard.addEventListener("click", flip);

document.addEventListener("keydown", (e) => {
  if (!cardsReady) return;
  if (e.key === " " || e.key === "Enter") {
    e.preventDefault();
    flip();
  } else if (e.key === "ArrowRight") {
    next();
  } else if (e.key === "ArrowLeft") {
    prev();
  }
});

setFiltersEnabled(false);
render();

fetch("cards.json")
  .then((r) => {
    if (!r.ok) throw new Error(`HTTP ${r.status}`);
    return r.json();
  })
  .then(onCardsLoaded)
  .catch((err) => {
    elCounter.textContent = "Load failed";
    elFront.textContent =
      "Failed to load cards.json. Run scripts/build_json.py or open via GitHub Pages.";
    console.error(err);
  });
