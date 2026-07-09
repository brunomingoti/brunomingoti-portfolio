import {
  IconBrandGithub,
  IconBrandLinkedin,
  IconDownload,
  IconMail,
  IconSchool,
  type Icon as TablerIcon,
} from "@tabler/icons-react";
import { useLanguage } from "../i18n/LanguageContext";
import type { ProfileData } from "../types";
import { withBase } from "../lib/assets";
import "./Contact.css";

export default function Contact({ profile }: { profile: ProfileData }) {
  const { ui } = useLanguage();

  const links = [
    { href: `mailto:${profile.email}`, label: profile.email, icon: IconMail },
    { href: profile.linkedinUrl, label: "LinkedIn", icon: IconBrandLinkedin },
    profile.githubUrl ? { href: profile.githubUrl, label: "GitHub", icon: IconBrandGithub } : null,
    { href: profile.scholarUrl, label: "Google Scholar", icon: IconSchool },
  ].filter(Boolean) as { href: string; label: string; icon: TablerIcon }[];

  return (
    <div className="page">
      <div className="container">
        <div className="section-head">
          <div>
            <span className="eyebrow">{ui.nav.contact}</span>
            <h2>{ui.nav.contact}</h2>
          </div>
        </div>

        <div className="contact-grid">
          <ul className="contact-links">
            {links.map((link) => (
              <li key={link.label}>
                <a href={link.href} target="_blank" rel="noreferrer">
                  <link.icon size={18} stroke={1.75} aria-hidden="true" />
                  {link.label}
                </a>
              </li>
            ))}
          </ul>

          <div className="cv-downloads">
            <a className="btn btn-primary" href={withBase(profile.cvPtUrl)} download>
              <IconDownload size={16} stroke={1.75} aria-hidden="true" /> {ui.contact.downloadPt}
            </a>
            <a className="btn" href={withBase(profile.cvEnUrl)} download>
              <IconDownload size={16} stroke={1.75} aria-hidden="true" /> {ui.contact.downloadEn}
            </a>
          </div>
        </div>
      </div>
    </div>
  );
}
