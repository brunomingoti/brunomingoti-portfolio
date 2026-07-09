import { Route, Routes } from "react-router-dom";
import Header from "./components/Header";
import Footer from "./components/Footer";
import Home from "./pages/Home";
import ProjectDetail from "./pages/ProjectDetail";
import content from "./data/content.json";
import type { ContentBundle } from "./types";

const typedContent = content as ContentBundle;

function App() {
  return (
    <>
      <Header />
      <main style={{ flex: 1 }}>
        <Routes>
          <Route path="/" element={<Home content={typedContent} />} />
          <Route path="/projetos/:slug" element={<ProjectDetail content={typedContent} />} />
        </Routes>
      </main>
      <Footer />
    </>
  );
}

export default App;
