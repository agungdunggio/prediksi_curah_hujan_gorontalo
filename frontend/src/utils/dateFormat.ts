const bulanIndo = [
    "Januari", "Februari", "Maret", "April", "Mei", "Juni",
    "Juli", "Agustus", "September", "Oktober", "November", "Desember"
  ];
  
  export function formatUpdatedAt(isoString: string | null): string {
    if (!isoString) return "-";
    const date = new Date(isoString);
    const jam = date.getHours().toString().padStart(2, "0");
    const menit = date.getMinutes().toString().padStart(2, "0");
    const hari = date.getDate();
    const bulan = bulanIndo[date.getMonth()];
    const tahun = date.getFullYear();
    return `${jam}:${menit} ${hari} ${bulan} ${tahun}`;
  }