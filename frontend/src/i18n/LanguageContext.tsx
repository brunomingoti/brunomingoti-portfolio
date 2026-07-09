import { createContext, useContext, useMemo, useState, type ReactNode } from "react";
import type { Bilingual, Lang } from "../types";

type UiStrings = typeof STRINGS["pt" | "en"];

interface LanguageContextValue {
  lang: Lang;
  toggleLang: () => void;
  t: (dict: Bilingual) => string;
  ui: UiStrings;
}

const STRINGS = {
  pt: {
    common: { backHome: "Início" },
    nav: { about: "Sobre", projects: "Projetos", publications: "Publicações", experience: "Experiência", contact: "Contato" },
    hero: { cta: "Ver projetos", contactCta: "Fale comigo" },
    projects: { all: "Todos", featured: "Destaque", viewCase: "Ver estudo de caso", back: "Voltar aos projetos" },
    publications: {
      paper: "Artigo",
      thesis: "TCC",
      report: "Relatório / código",
    },
    contact: {
      downloadPt: "Currículo (PT)",
      downloadEn: "Resume (EN)",
    },
  },
  en: {
    common: { backHome: "Home" },
    nav: { about: "About", projects: "Projects", publications: "Publications", experience: "Experience", contact: "Contact" },
    hero: { cta: "View projects", contactCta: "Get in touch" },
    projects: { all: "All", featured: "Featured", viewCase: "View case study", back: "Back to projects" },
    publications: {
      paper: "Paper",
      thesis: "Thesis",
      report: "Report / code",
    },
    contact: {
      downloadPt: "Currículo (PT)",
      downloadEn: "Resume (EN)",
    },
  },
} as const;

const LanguageContext = createContext<LanguageContextValue | null>(null);

function detectInitialLang(): Lang {
  const saved = localStorage.getItem("lang");
  if (saved === "pt" || saved === "en") return saved;
  return "en";
}

export function LanguageProvider({ children }: { children: ReactNode }) {
  const [lang, setLang] = useState<Lang>(detectInitialLang);

  const value = useMemo<LanguageContextValue>(
    () => ({
      lang,
      toggleLang: () =>
        setLang((prev) => {
          const next = prev === "pt" ? "en" : "pt";
          localStorage.setItem("lang", next);
          return next;
        }),
      t: (dict: Bilingual) => dict[lang],
      ui: STRINGS[lang],
    }),
    [lang]
  );

  return <LanguageContext.Provider value={value}>{children}</LanguageContext.Provider>;
}

export function useLanguage() {
  const ctx = useContext(LanguageContext);
  if (!ctx) throw new Error("useLanguage must be used within LanguageProvider");
  return ctx;
}
