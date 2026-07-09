import { Link, NavLink } from "react-router-dom";
import { IconLanguage } from "@tabler/icons-react";
import { useLanguage } from "../i18n/LanguageContext";
import "./Header.css";

export default function Header() {
  const { ui, lang, toggleLang } = useLanguage();

  const links = [
    { to: "/sobre", label: ui.nav.about },
    { to: "/projetos", label: ui.nav.projects },
    { to: "/publicacoes", label: ui.nav.publications },
    { to: "/experiencia", label: ui.nav.experience },
    { to: "/contato", label: ui.nav.contact },
  ];

  return (
    <header className="site-header">
      <div className="container site-header-inner">
        <Link to="/" className="brand">
          <span className="brand-mark">BM</span>
          <span className="brand-name">Bruno Mingoti</span>
        </Link>
        <nav className="site-nav">
          {links.map((l) => (
            <NavLink key={l.to} to={l.to} className={({ isActive }) => (isActive ? "active" : "")}>
              {l.label}
            </NavLink>
          ))}
        </nav>
        <button className="lang-toggle" onClick={toggleLang} aria-label="Toggle language">
          <IconLanguage size={16} stroke={1.75} aria-hidden="true" />
          {lang === "pt" ? "PT" : "EN"}
        </button>
      </div>
    </header>
  );
}
