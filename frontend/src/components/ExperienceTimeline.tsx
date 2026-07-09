import { useLanguage } from "../i18n/LanguageContext";
import type { EducationData, ExperienceData } from "../types";
import "./ExperienceTimeline.css";

export default function ExperienceTimeline({
  experience,
  education,
}: {
  experience: ExperienceData[];
  education: EducationData[];
}) {
  const { t, ui, lang } = useLanguage();

  return (
    <div className="page">
      <div className="container">
        <div className="section-head">
          <div>
            <span className="eyebrow">{ui.nav.experience}</span>
            <h2>{ui.nav.experience}</h2>
          </div>
        </div>

        <div className="experience-grid">
          <div>
            <h3 className="timeline-heading">{lang === "pt" ? "Experiência" : "Experience"}</h3>
            <ol className="timeline">
              {experience.map((exp) => (
                <li key={exp.organization} className="timeline-item">
                  <div className="timeline-dot" />
                  <div className="timeline-content">
                    <div className="timeline-top">
                      <h3>{exp.organization}</h3>
                      <span className="timeline-period">
                        {exp.periodStart} — {exp.periodEnd}
                      </span>
                    </div>
                    <p className="timeline-role">
                      {t(exp.role)} {exp.location && `· ${exp.location}`}
                    </p>
                    {t(exp.context) && <p className="timeline-context">{t(exp.context)}</p>}
                    <ul className="timeline-highlights">
                      {(lang === "pt" ? exp.highlights.pt : exp.highlights.en).map((h, i) => (
                        <li key={i}>{h}</li>
                      ))}
                    </ul>
                    {exp.tools.length > 0 && (
                      <div className="timeline-tools">
                        {exp.tools.map((tool) => (
                          <span className="pill" key={tool}>
                            {tool}
                          </span>
                        ))}
                      </div>
                    )}
                  </div>
                </li>
              ))}
            </ol>
          </div>

          <div>
            <h3 className="timeline-heading">{lang === "pt" ? "Educação" : "Education"}</h3>
            <ol className="timeline">
              {education.map((ed) => (
                <li key={ed.institution} className="timeline-item">
                  <div className="timeline-dot timeline-dot-alt" />
                  <div className="timeline-content">
                    <div className="timeline-top">
                      <h3>{ed.institution}</h3>
                      <span className="timeline-period">
                        {ed.periodStart} — {ed.periodEnd}
                      </span>
                    </div>
                    <p className="timeline-role">
                      {t(ed.degree)} {ed.location && `· ${ed.location}`}
                    </p>
                    <ul className="timeline-highlights">
                      {(lang === "pt" ? ed.details.pt : ed.details.en).map((h, i) => (
                        <li key={i}>{h}</li>
                      ))}
                    </ul>
                  </div>
                </li>
              ))}
            </ol>
          </div>
        </div>
      </div>
    </div>
  );
}
