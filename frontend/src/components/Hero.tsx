import { IconArrowDown, IconTerminal2 } from "@tabler/icons-react";
import { useLanguage } from "../i18n/LanguageContext";
import type { ProfileData } from "../types";
import "./Hero.css";

export default function Hero({ profile }: { profile: ProfileData }) {
  const { t, ui, lang } = useLanguage();

  return (
    <section className="hero">
      <div className="container hero-inner">
        <span className="eyebrow eyebrow-icon">
          <IconTerminal2 size={16} stroke={1.75} aria-hidden="true" /> {lang === "pt" ? "Portfólio" : "Portfolio"}
        </span>
        <h1>{profile.name}</h1>
        <p className="hero-headline">{t(profile.headline)}</p>
        <div className="hero-actions">
          <a className="btn btn-primary" href="#projects">
            {ui.hero.cta} <IconArrowDown size={16} stroke={1.75} aria-hidden="true" />
          </a>
          <a className="btn" href="#contact">
            {ui.hero.contactCta}
          </a>
        </div>
        <div className="hero-tags">
          {["Python", "TypeScript", "PyTorch", "OpenCV", "React", "Docker"].map((tag) => (
            <span className="pill" key={tag}>
              {tag}
            </span>
          ))}
        </div>
      </div>
    </section>
  );
}
