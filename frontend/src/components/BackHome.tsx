import { Link } from "react-router-dom";
import { IconArrowLeft } from "@tabler/icons-react";
import { useLanguage } from "../i18n/LanguageContext";

export default function BackHome() {
  const { ui } = useLanguage();
  return (
    <Link to="/" className="back-link">
      <IconArrowLeft size={16} stroke={1.75} aria-hidden="true" /> {ui.common.backHome}
    </Link>
  );
}
