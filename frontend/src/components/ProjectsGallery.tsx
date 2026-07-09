import { useMemo, useState } from "react";
import { useLanguage } from "../i18n/LanguageContext";
import type { InstitutionData, ProjectData } from "../types";
import ProjectCard from "./ProjectCard";
import "./ProjectsGallery.css";

export default function ProjectsGallery({
  projects,
  institutions,
}: {
  projects: ProjectData[];
  institutions: InstitutionData[];
}) {
  const { ui } = useLanguage();
  const [filter, setFilter] = useState<string>("all");

  const institutionMap = useMemo(
    () => Object.fromEntries(institutions.map((i) => [i.slug, i.name])),
    [institutions]
  );

  const filtered = useMemo(() => {
    if (filter === "all") return projects;
    if (filter === "featured") return projects.filter((p) => p.featured);
    return projects.filter((p) => p.institution === filter);
  }, [projects, filter]);

  return (
    <div className="page">
      <div className="container">
        <div className="section-head">
          <div>
            <span className="eyebrow">{ui.nav.projects}</span>
            <h2>{ui.nav.projects}</h2>
          </div>
          <div className="filter-row">
            <button
              className={`filter-chip ${filter === "all" ? "active" : ""}`}
              onClick={() => setFilter("all")}
            >
              {ui.projects.all}
            </button>
            <button
              className={`filter-chip ${filter === "featured" ? "active" : ""}`}
              onClick={() => setFilter("featured")}
            >
              {ui.projects.featured}
            </button>
            {institutions.map((inst) => (
              <button
                key={inst.slug}
                className={`filter-chip ${filter === inst.slug ? "active" : ""}`}
                onClick={() => setFilter(inst.slug)}
              >
                {inst.name}
              </button>
            ))}
          </div>
        </div>
        <div className="project-grid">
          {filtered.map((project) => (
            <ProjectCard
              key={project.slug}
              project={project}
              institutionName={institutionMap[project.institution] ?? project.institution}
            />
          ))}
        </div>
      </div>
    </div>
  );
}
