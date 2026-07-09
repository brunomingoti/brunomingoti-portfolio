import { Route, Routes } from "react-router-dom";
import Header from "./components/Header";
import Footer from "./components/Footer";
import Home from "./pages/Home";
import ProjectDetail from "./pages/ProjectDetail";
import About from "./components/About";
import ProjectsGallery from "./components/ProjectsGallery";
import Publications from "./components/Publications";
import ExperienceTimeline from "./components/ExperienceTimeline";
import Contact from "./components/Contact";
import content from "./data/content.json";
import type { ContentBundle } from "./types";

const typedContent = content as ContentBundle;

function App() {
  return (
    <>
      <Header />
      <main style={{ flex: 1, minHeight: 0, overflowY: "auto" }}>
        <Routes>
          <Route path="/" element={<Home content={typedContent} />} />
          <Route path="/sobre" element={<About profile={typedContent.profile} />} />
          <Route
            path="/projetos"
            element={
              <ProjectsGallery projects={typedContent.projects} institutions={typedContent.institutions} />
            }
          />
          <Route path="/projetos/:slug" element={<ProjectDetail content={typedContent} />} />
          <Route path="/publicacoes" element={<Publications publications={typedContent.publications} />} />
          <Route
            path="/experiencia"
            element={
              <ExperienceTimeline experience={typedContent.experience} education={typedContent.education} />
            }
          />
          <Route path="/contato" element={<Contact profile={typedContent.profile} />} />
        </Routes>
      </main>
      <Footer />
    </>
  );
}

export default App;
