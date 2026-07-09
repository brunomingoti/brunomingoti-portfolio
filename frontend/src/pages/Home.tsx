import Hero from "../components/Hero";
import About from "../components/About";
import ProjectsGallery from "../components/ProjectsGallery";
import Publications from "../components/Publications";
import ExperienceTimeline from "../components/ExperienceTimeline";
import Contact from "../components/Contact";
import type { ContentBundle } from "../types";

export default function Home({ content }: { content: ContentBundle }) {
  return (
    <>
      <Hero profile={content.profile} />
      <About profile={content.profile} />
      <ProjectsGallery projects={content.projects} institutions={content.institutions} />
      <Publications publications={content.publications} />
      <ExperienceTimeline experience={content.experience} education={content.education} />
      <Contact profile={content.profile} />
    </>
  );
}
