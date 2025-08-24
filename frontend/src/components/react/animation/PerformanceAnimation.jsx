// src/components/react/animation/PerformanceAnimation.jsx
import { useEffect } from "react";
import gsap from "gsap";
import { ScrollTrigger } from "gsap/ScrollTrigger";

export default function PerformanceAnimation() {
  useEffect(() => {
    gsap.registerPlugin(ScrollTrigger);

    const ctx = gsap.context(() => {
      const section = document.querySelector("#model-performance");
      if (!section) return;

      const heading = section.querySelector("h2");
      const desc = section.querySelector("p.text-gray-300");
      const cards = gsap.utils.toArray(".metric-card");
      const icons = gsap.utils.toArray(".metric-card .metric-icon");
      const values = gsap.utils.toArray(".metric-card .metric-value");
      const blobs = ["#blob-1", "#blob-2", "#blob-3"];

      // State awal (tanpa andalkan Tailwind)
      gsap.set([heading, desc], { autoAlpha: 0, y: 24 });
      gsap.set(cards, { autoAlpha: 0, y: 28, scale: 0.98 });
      gsap.set(icons, { autoAlpha: 0, y: 10, rotate: -8 });
      values.forEach(v => gsap.set(v, { textContent: "0.0000" }));

      // Timeline saat section masuk viewport
      const tl = gsap.timeline({
        defaults: { ease: "power3.out" },
        scrollTrigger: {
          trigger: section,
          start: "top 70%",
          end: "bottom 40%",
          once: true,
        },
      });

      tl.to(heading, { autoAlpha: 1, y: 0, duration: 1.2 })
        .to(desc, { autoAlpha: 1, y: 0, duration: 0.6 }, "-=0.35")
        .to(cards, {
          autoAlpha: 1,
          y: 0,
          scale: 1,
          duration: 0.6,
          stagger: { each: 0.15, from: "start" },
        }, "-=0.2")
        .to(icons, {
          autoAlpha: 1,
          y: 0,
          rotate: 0,
          duration: 0.5,
          stagger: { each: 0.15, from: "start" },
        }, "-=0.4");

      // Count-up angka dengan format Indonesia
      values.forEach((el, idx) => {
        const target = parseFloat(el.dataset.value || "0"); // pakai . (titik) sebagai desimal
        const dur = 1.2 + idx * 0.1;
        const obj = { val: 0 };
        const fmt = new Intl.NumberFormat("id-ID", {
          minimumFractionDigits: 4,
          maximumFractionDigits: 4,
        });

        tl.to(obj, {
          val: target,
          duration: dur,
          ease: "power2.out",
          onUpdate: () => {
            el.textContent = fmt.format(obj.val);
          },
        }, "-=0.9"); // mulai sedikit overlap dengan animasi kartu
      });

      // Blob background “mengambang”
      blobs.forEach((sel, i) => {
        const b = document.querySelector(sel);
        if (!b) return;
        gsap.to(b, {
          y: i % 2 === 0 ? 25 : -25,
          x: i === 1 ? -18 : 18,
          scale: 1.03,
          duration: 6 + i * 1.5,
          ease: "sine.inOut",
          yoyo: true,
          repeat: -1,
        });
      });
    });

    return () => ctx.revert();
  }, []);

  return null;
}
