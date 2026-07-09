import BackHome from "./BackHome";
import { useLanguage } from "../i18n/LanguageContext";
import type { ProfileData } from "../types";
import "./About.css";

export default function About({ profile }: { profile: ProfileData }) {
  const { t, ui } = useLanguage();
  const paragraphs = t(profile.bio).split("\n\n");

  return (
    <div className="page">
      <div className="container">
        <BackHome />
        <div className="section-head">
          <div>
            <span className="eyebrow">{ui.nav.about}</span>
            <h2>{ui.nav.about}</h2>
          </div>
        </div>
        <div className="about-body">
          {paragraphs.map((p, i) => (
            <p key={i}>{p}</p>
          ))}
        </div>
      </div>
    </div>
  );
}
