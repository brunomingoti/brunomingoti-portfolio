import { Link, useLocation } from "react-router-dom";
import { IconLanguage } from "@tabler/icons-react";
import { useLanguage } from "../i18n/LanguageContext";
import "./Header.css";

export default function Header() {
  const { ui, lang, toggleLang } = useLanguage();
  const location = useLocation();
  const isHome = location.pathname === "/" || location.pathname === "";

  const links = [
    { to: "/#about", label: ui.nav.about },
    { to: "/#projects", label: ui.nav.projects },
    { to: "/#publications", label: ui.nav.publications },
    { to: "/#experience", label: ui.nav.experience },
    { to: "/#contact", label: ui.nav.contact },
  ];

  return (
    <header className="site-header">
      <div className="container site-header-inner">
        <Link to="/" className="brand">
          <span className="brand-mark">BM</span>
          <span className="brand-name">Bruno Mingoti</span>
        </Link>
        {isHome && (
          <nav className="site-nav">
            {links.map((l) => (
              <a key={l.to} href={`#${l.to.split("#")[1]}`}>
                {l.label}
              </a>
            ))}
          </nav>
        )}
        <button className="lang-toggle" onClick={toggleLang} aria-label="Toggle language">
          <IconLanguage size={16} stroke={1.75} aria-hidden="true" />
          {lang === "pt" ? "PT" : "EN"}
        </button>
      </div>
    </header>
  );
}
