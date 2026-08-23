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

function applyFilters() {
  const domain = elDomain.value;
  const scenario = elScenario.value;
  const task = elTask.value;
  filtered = allCards.filter((c) => {
    if (domain && c.domain !== domain) return false;
    if (scenario) {
      const scenarios = c.scenarios || [];
      if (!scenarios.includes(scenario) && !scenarios.includes("all")) return false;
    }
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

function populateTaskFilter() {
  const tasks = new Set();
  for (const card of allCards) {
    for (const t of card.tasks || []) {
      tasks.add(t);
    }
  }
  const sorted = [...tasks].sort((a, b) => {
    const parse = (x) => {
      if (/^[1-5]\.\d$/.test(x)) {
        const [d, t] = x.split(".").map(Number);
        return [0, d, t];
      }
      return [1, 0, x];
    };
    const pa = parse(a);
    const pb = parse(b);
    return pa[0] - pb[0] || pa[1] - pb[1] || pa[2] - pb[2] || String(a).localeCompare(String(b));
  });
  for (const t of sorted) {
    const opt = document.createElement("option");
    opt.value = t;
    opt.textContent = t;
    elTask.appendChild(opt);
  }
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
  elBack.innerHTML = `<strong>A:</strong> ${card.back}` +
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

document.getElementById("flip-btn").addEventListener("click", flip);
document.getElementById("next-btn").addEventListener("click", next);
document.getElementById("prev-btn").addEventListener("click", prev);
document.getElementById("shuffle-btn").addEventListener("click", shuffle);
elDomain.addEventListener("change", applyFilters);
elScenario.addEventListener("change", applyFilters);
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
    populateTaskFilter();
    const params = new URLSearchParams(window.location.search);
    const domain = params.get("domain");
    const scenario = params.get("scenario");
    const task = params.get("task");
    if (domain) elDomain.value = domain;
    if (scenario) elScenario.value = scenario;
    if (task) elTask.value = task;
    if (domain || scenario || task) {
      applyFilters();
    } else {
      filtered = [...allCards];
      render();
    }
  })
  .catch((err) => {
    elFront.textContent = "Failed to load cards.json. Run scripts/build_json.py first.";
    console.error(err);
  });
