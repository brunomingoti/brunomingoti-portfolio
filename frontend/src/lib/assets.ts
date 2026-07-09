export function withBase(path: string): string {
  if (!path) return path;
  const base = import.meta.env.BASE_URL.replace(/\/$/, "");
  return path.startsWith("/") ? `${base}${path}` : `${base}/${path}`;
}
