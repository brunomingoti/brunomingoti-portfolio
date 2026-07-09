import { Link } from "react-router-dom";
import { useLanguage } from "../i18n/LanguageContext";
import type { ProjectData } from "../types";
import { withBase } from "../lib/assets";
import Icon from "./Icon";
import "./ProjectCard.css";

export default function ProjectCard({
  project,
  institutionName,
}: {
  project: ProjectData;
  institutionName: string;
}) {
  const { t } = useLanguage();

  return (
    <Link to={`/projetos/${project.slug}`} className="project-card">
      <div className="project-card-media">
        {project.coverImage ? (
          <img src={withBase(project.coverImage)} alt="" loading="lazy" />
        ) : (
          <Icon name={project.icon} size={34} />
        )}
        {project.featured && <span className="project-card-badge">★</span>}
      </div>
      <div className="project-card-body">
        <span className="project-card-inst">{institutionName}</span>
        <h3>{t(project.title)}</h3>
        <p>{t(project.summary)}</p>
      </div>
    </Link>
  );
}
