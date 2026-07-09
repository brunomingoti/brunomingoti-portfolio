import {
  IconBattery2,
  IconCertificate,
  IconChartDots,
  IconCode,
  IconCpu,
  IconDeviceLaptop,
  IconDrone,
  IconFileSpreadsheet,
  IconFlame,
  IconMicroscope,
  IconScan,
  IconTopologyStar3,
  type Icon as TablerIcon,
} from "@tabler/icons-react";

const ICON_MAP: Record<string, TablerIcon> = {
  "ti-scan": IconScan,
  "ti-topology-star-3": IconTopologyStar3,
  "ti-certificate": IconCertificate,
  "ti-drone": IconDrone,
  "ti-flame": IconFlame,
  "ti-cpu": IconCpu,
  "ti-device-laptop": IconDeviceLaptop,
  "ti-chart-dots": IconChartDots,
  "ti-microscope": IconMicroscope,
  "ti-battery-2": IconBattery2,
  "ti-file-spreadsheet": IconFileSpreadsheet,
  "ti-code": IconCode,
};

export default function Icon({
  name,
  size = 18,
  className,
}: {
  name: string;
  size?: number;
  className?: string;
}) {
  const Component = ICON_MAP[name] ?? IconCode;
  return <Component size={size} stroke={1.75} className={className} aria-hidden="true" />;
}
