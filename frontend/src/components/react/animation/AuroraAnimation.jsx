import { useEffect } from 'react';
import gsap from 'gsap';

export default function AuroraAnimation() {
  useEffect(() => {
    // Fungsi untuk menganimasikan satu blob secara acak dan terus-menerus
    const animateBlob = (selector) => {
      gsap.to(selector, {
        x: gsap.utils.random(-50, 50, true), // Bergerak acak sumbu X
        y: gsap.utils.random(-50, 50, true), // Bergerak acak sumbu Y
        scale: gsap.utils.random(0.8, 1.2, true),
        duration: gsap.utils.random(10, 20, true), // Durasi acak
        repeat: -1, // Ulangi selamanya
        yoyo: true, // Kembali ke posisi semula dengan mulus
        ease: 'sine.inOut',
      });
    };

    // Jalankan animasi untuk setiap blob
    animateBlob('#blob-1');
    animateBlob('#blob-2');
    animateBlob('#blob-3');
  }, []);

  return null; // Komponen ini tidak me-render apapun
}