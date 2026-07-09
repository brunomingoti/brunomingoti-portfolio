import { Link } from "react-router-dom";
import {
  IconArrowRight,
  IconMailFast,
  IconNotebook,
  IconTimeline,
  IconUser,
} from "@tabler/icons-react";
import Hero from "../components/Hero";
import ProjectCard from "../components/ProjectCard";
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
  const { ui } = useLanguage();
  const institutionMap = Object.fromEntries(content.institutions.map((i) => [i.slug, i.name]));
  const featured = content.projects.filter((p) => p.featured).slice(0, 3);

  return (
    <>
      <Hero profile={content.profile} />

      <div className="page home-page">
        <div className="container">
          <div className="quick-links">
            {QUICK_LINKS.map(({ to, icon: Icon, key }) => (
              <Link key={to} to={to} className="quick-link-card">
                <Icon size={22} stroke={1.75} aria-hidden="true" />
                <span>{ui.nav[key]}</span>
                <IconArrowRight size={16} stroke={1.75} className="quick-link-arrow" aria-hidden="true" />
              </Link>
            ))}
          </div>

          <div className="section-head home-featured-head">
            <div>
              <span className="eyebrow">{ui.projects.featured}</span>
              <h2>{ui.nav.projects}</h2>
            </div>
            <Link to="/projetos" className="btn">
              {ui.projects.all} <IconArrowRight size={16} stroke={1.75} aria-hidden="true" />
            </Link>
          </div>

          <div className="project-grid">
            {featured.map((project) => (
              <ProjectCard
                key={project.slug}
                project={project}
                institutionName={institutionMap[project.institution] ?? project.institution}
              />
            ))}
          </div>
        </div>
      </div>
    </>
  );
}
