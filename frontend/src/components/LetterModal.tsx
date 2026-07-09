import { useEffect } from "react";
import { IconExternalLink, IconX } from "@tabler/icons-react";
import { withBase } from "../lib/assets";
import "./LetterModal.css";

const IMAGE_EXT = [".jpg", ".jpeg", ".png", ".webp", ".gif"];

export default function LetterModal({
  url,
  title,
  onClose,
}: {
  url: string;
  title: string;
  onClose: () => void;
}) {
  useEffect(() => {
    const onKey = (e: KeyboardEvent) => e.key === "Escape" && onClose();
    document.addEventListener("keydown", onKey);
    document.body.style.overflow = "hidden";
    return () => {
      document.removeEventListener("keydown", onKey);
      document.body.style.overflow = "";
    };
  }, [onClose]);

  const fullUrl = withBase(url);
  const isImage = IMAGE_EXT.some((ext) => url.toLowerCase().endsWith(ext));

  return (
    <div className="letter-modal-overlay" onClick={onClose}>
      <div className="letter-modal" onClick={(e) => e.stopPropagation()}>
        <div className="letter-modal-head">
          <h3>{title}</h3>
          <div className="letter-modal-actions">
            <a href={fullUrl} target="_blank" rel="noreferrer" className="btn">
              <IconExternalLink size={16} stroke={1.75} aria-hidden="true" />
            </a>
            <button className="btn" onClick={onClose} aria-label="Fechar">
              <IconX size={16} stroke={1.75} aria-hidden="true" />
            </button>
          </div>
        </div>
        <div className="letter-modal-body">
          {isImage ? (
            <img src={fullUrl} alt={title} />
          ) : (
            <iframe src={fullUrl} title={title} />
          )}
        </div>
      </div>
    </div>
  );
}
