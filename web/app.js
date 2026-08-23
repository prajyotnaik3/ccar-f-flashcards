let allCards = [];
let filtered = [];
let index = 0;
let flipped = false;

const elDomain = document.getElementById("filter-domain");
const elScenario = document.getElementById("filter-scenario");
const elCounter = document.getElementById("counter");
const elMeta = document.getElementById("card-meta");
const elFront = document.getElementById("card-front");
const elBack = document.getElementById("card-back");
const elCard = document.getElementById("card");

function applyFilters() {
  const domain = elDomain.value;
  const scenario = elScenario.value;
  filtered = allCards.filter((c) => {
    if (domain && c.domain !== domain) return false;
    if (scenario) {
      const scenarios = c.scenarios || [];
      if (!scenarios.includes(scenario) && !scenarios.includes("all")) return false;
    }
    return true;
  });
  index = 0;
  flipped = false;
  render();
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
  elMeta.textContent = `${card.id} · ${card.domain} · ${card.type} · ${(card.scenarios || []).join(", ")}`;
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
    const params = new URLSearchParams(window.location.search);
    const domain = params.get("domain");
    const scenario = params.get("scenario");
    if (domain) elDomain.value = domain;
    if (scenario) elScenario.value = scenario;
    if (domain || scenario) {
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
