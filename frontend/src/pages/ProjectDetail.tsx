import { Link, Navigate, useParams } from "react-router-dom";
import { IconArrowLeft, IconExternalLink, IconPlayerPlay } from "@tabler/icons-react";
import { useLanguage } from "../i18n/LanguageContext";
import type { ContentBundle } from "../types";
import { withBase } from "../lib/assets";
import "./ProjectDetail.css";

export default function ProjectDetail({ content }: { content: ContentBundle }) {
  const { slug } = useParams();
  const { t, ui } = useLanguage();
  const project = content.projects.find((p) => p.slug === slug);

  if (!project) return <Navigate to="/" replace />;

  const institution = content.institutions.find((i) => i.slug === project.institution);
  const paragraphs = t(project.body).split("\n\n");

  return (
    <article className="case-study">
      <div className="container">
        <Link to="/projetos" className="case-study-back">
          <IconArrowLeft size={16} stroke={1.75} aria-hidden="true" /> {ui.projects.back}
        </Link>

        <header className="case-study-head">
          <span className="eyebrow">{institution?.name}</span>
          <h1>{t(project.title)}</h1>
          <p className="case-study-summary">{t(project.summary)}</p>

          <dl className="case-study-meta">
            <div>
              <dt>Papel / Role</dt>
              <dd>{t(project.role)}</dd>
            </div>
            <div>
              <dt>Período / Timeline</dt>
              <dd>
                {project.periodStart} — {project.periodEnd}
              </dd>
            </div>
          </dl>

          {project.tools.length > 0 && (
            <div className="case-study-tools">
              {project.tools.map((tool) => (
                <span className="pill" key={tool}>
                  {tool}
                </span>
              ))}
            </div>
          )}

          {(project.repoUrl || project.demoUrl) && (
            <div className="case-study-links">
              {project.repoUrl && (
                <a className="btn" href={project.repoUrl} target="_blank" rel="noreferrer">
                  <IconExternalLink size={16} stroke={1.75} aria-hidden="true" /> Repositório / Zenodo
                </a>
              )}
              {project.demoUrl && (
                <a className="btn" href={project.demoUrl} target="_blank" rel="noreferrer">
                  <IconPlayerPlay size={16} stroke={1.75} aria-hidden="true" /> Demo
                </a>
              )}
            </div>
          )}
        </header>

        {project.coverImage && (
          <div className="case-study-cover">
            <img src={withBase(project.coverImage)} alt="" />
          </div>
        )}

        <div className="case-study-body">
          {paragraphs.map((p, i) => (
            <p key={i}>{p}</p>
          ))}
        </div>

        {project.images.length > 0 && (
          <div className="case-study-gallery">
            {project.images.map((img, i) => (
              <figure key={i}>
                <img src={withBase(img.src)} alt={t(img.caption)} />
                {t(img.caption) && <figcaption>{t(img.caption)}</figcaption>}
              </figure>
            ))}
          </div>
        )}
      </div>
    </article>
  );
}
