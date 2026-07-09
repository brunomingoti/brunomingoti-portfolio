import "./Footer.css";

export default function Footer() {
  return (
    <footer className="site-footer">
      <div className="container">
        <p>© {new Date().getFullYear()} Bruno Mingoti</p>
      </div>
    </footer>
  );
}
