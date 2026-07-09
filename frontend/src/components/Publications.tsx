import { IconCode, IconExternalLink, IconFileText, IconSchool } from "@tabler/icons-react";
import { useLanguage } from "../i18n/LanguageContext";
import type { PublicationData } from "../types";
import "./Publications.css";

const TYPE_ICON: Record<PublicationData["type"], typeof IconFileText> = {
  paper: IconFileText,
  thesis: IconSchool,
  report: IconCode,
};

export default function Publications({ publications }: { publications: PublicationData[] }) {
  const { t, ui } = useLanguage();

  return (
    <div className="page">
      <div className="container">
        <div className="section-head">
          <div>
            <span className="eyebrow">{ui.nav.publications}</span>
            <h2>{ui.nav.publications}</h2>
          </div>
        </div>
        <ul className="pub-list">
          {publications.map((pub) => {
            const TypeIcon = TYPE_ICON[pub.type];
            return (
            <li key={pub.title} className="pub-item">
              <div className="pub-icon">
                <TypeIcon size={20} stroke={1.75} aria-hidden="true" />
              </div>
              <div className="pub-body">
                <div className="pub-top">
                  <h3>{pub.title}</h3>
                  <span className="pill">{ui.publications[pub.type]}</span>
                </div>
                <p className="pub-venue">
                  {pub.venue} · {pub.year}
                  {pub.authors ? ` · ${pub.authors}` : ""}
                </p>
                {t(pub.summary) && <p className="pub-summary">{t(pub.summary)}</p>}
                {pub.url && (
                  <a className="pub-link" href={pub.url} target="_blank" rel="noreferrer">
                    <IconExternalLink size={14} stroke={1.75} aria-hidden="true" />{" "}
                    {pub.url.includes("zenodo") ? "Zenodo" : "Google Scholar"}
                  </a>
                )}
              </div>
            </li>
            );
          })}
        </ul>
      </div>
    </div>
  );
}
