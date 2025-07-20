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
    return `${jam}:${menit}, ${hari} ${bulan} ${tahun}`;
}
export function formatTanggalTooltip(dateString: string | null): string {
    if (!dateString) return "-";
    const date = new Date(`${dateString}T00:00:00`); 
    const hari = date.getDate(); // Tanpa padStart, jadi "1" bukan "01"
    const bulan = bulanIndo[date.getMonth()];
    const tahun = date.getFullYear();
    return `${hari} ${bulan} ${tahun}`;
}