import { Link } from "react-router-dom";
import {
  IconArrowRight,
  IconMailFast,
  IconNotebook,
  IconTimeline,
  IconUser,
} from "@tabler/icons-react";
import Hero from "../components/Hero";
import ProjectIcon from "../components/Icon";
import { useLanguage } from "../i18n/LanguageContext";
import type { ContentBundle } from "../types";
import "./Home.css";

const QUICK_LINKS = [
  { to: "/sobre", icon: IconUser, key: "about" as const },
  { to: "/publicacoes", icon: IconNotebook, key: "publications" as const },
  { to: "/experiencia", icon: IconTimeline, key: "experience" as const },
  { to: "/contato", icon: IconMailFast, key: "contact" as const },
];

export default function Home({ content }: { content: ContentBundle }) {
  const { t, ui } = useLanguage();
  const institutionMap = Object.fromEntries(content.institutions.map((i) => [i.slug, i.name]));
  const featured = content.projects.filter((p) => p.featured).slice(0, 4);

  return (
    <div className="page home-page">
      <div className="container">
        <div className="home-grid">
          <div className="home-hero-col">
            <Hero profile={content.profile} />
          </div>

          <div className="home-side-col">
            <div className="quick-links">
              {QUICK_LINKS.map(({ to, icon: Icon, key }) => (
                <Link key={to} to={to} className="quick-link-card">
                  <Icon size={18} stroke={1.75} aria-hidden="true" />
                  <span>{ui.nav[key]}</span>
                  <IconArrowRight size={14} stroke={1.75} className="quick-link-arrow" aria-hidden="true" />
                </Link>
              ))}
            </div>

            <div className="home-featured">
              <div className="section-head home-featured-head">
                <span className="eyebrow">{ui.projects.featured}</span>
                <Link to="/projetos" className="home-featured-all">
                  {ui.projects.all} <IconArrowRight size={14} stroke={1.75} aria-hidden="true" />
                </Link>
              </div>
              <ul className="home-featured-list">
                {featured.map((project) => (
                  <li key={project.slug}>
                    <Link to={`/projetos/${project.slug}`} className="home-featured-item">
                      <span className="home-featured-icon">
                        <ProjectIcon name={project.icon} size={16} />
                      </span>
                      <span className="home-featured-text">
                        <strong>{t(project.title)}</strong>
                        <span>{institutionMap[project.institution] ?? project.institution}</span>
                      </span>
                    </Link>
                  </li>
                ))}
              </ul>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
