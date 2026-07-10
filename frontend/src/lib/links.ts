const KNOWN_HOSTS: { match: (host: string) => boolean; label: string }[] = [
  { match: (h) => h.includes("zenodo.org"), label: "Zenodo" },
  { match: (h) => h.includes("scholar.google"), label: "Google Scholar" },
  { match: (h) => h.includes("doi.org"), label: "DOI" },
  { match: (h) => h.includes("arxiv.org"), label: "arXiv" },
  { match: (h) => h.includes("github.com"), label: "GitHub" },
  { match: (h) => h.includes("ieee.org"), label: "IEEE Xplore" },
  { match: (h) => h.includes("researchgate.net"), label: "ResearchGate" },
  { match: (h) => h.includes("sbc.org.br"), label: "SBC" },
];

export function linkLabel(url: string, fallback: string): string {
  try {
    const host = new URL(url).hostname.toLowerCase();
    const known = KNOWN_HOSTS.find((entry) => entry.match(host));
    return known ? known.label : fallback;
  } catch {
    return fallback;
  }
}
