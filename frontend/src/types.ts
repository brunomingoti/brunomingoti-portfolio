export type Lang = "pt" | "en";

export interface Bilingual {
  pt: string;
  en: string;
}

export interface ProfileData {
  name: string;
  headline: Bilingual;
  bio: Bilingual;
  email: string;
  phone: string;
  linkedinUrl: string;
  githubUrl: string;
  scholarUrl: string;
  photoUrl: string;
  cvPtUrl: string;
  cvEnUrl: string;
}

export interface InstitutionData {
  slug: string;
  name: string;
}

export interface ProjectImageData {
  src: string;
  caption: Bilingual;
}

export interface ProjectData {
  slug: string;
  title: Bilingual;
  summary: Bilingual;
  body: Bilingual;
  institution: string;
  role: Bilingual;
  periodStart: string;
  periodEnd: string;
  tools: string[];
  icon: string;
  coverImage: string;
  repoUrl: string;
  demoUrl: string;
  featured: boolean;
  images: ProjectImageData[];
}

export interface PublicationData {
  title: string;
  authors: string;
  venue: string;
  year: number;
  type: "paper" | "thesis" | "report";
  url: string;
  summary: Bilingual;
}

export interface ExperienceData {
  organization: string;
  location: string;
  role: Bilingual;
  periodStart: string;
  periodEnd: string;
  context: Bilingual;
  highlights: { pt: string[]; en: string[] };
  tools: string[];
  recommendationLetters: { url: string; label: Bilingual }[];
}

export interface EducationData {
  institution: string;
  location: string;
  degree: Bilingual;
  periodStart: string;
  periodEnd: string;
  details: { pt: string[]; en: string[] };
}

export interface ContentBundle {
  profile: ProfileData;
  institutions: InstitutionData[];
  projects: ProjectData[];
  publications: PublicationData[];
  experience: ExperienceData[];
  education: EducationData[];
}
