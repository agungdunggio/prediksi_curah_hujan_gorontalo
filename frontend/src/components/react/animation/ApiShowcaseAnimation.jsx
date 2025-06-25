import { useEffect } from "react";
import gsap from "gsap";
import { ScrollTrigger } from "gsap/ScrollTrigger";

export default function ApiShowcaseAnimation() {
  useEffect(() => {
    const run = async () => {
      try {
        gsap.registerPlugin(ScrollTrigger);

        // Header animasi
        gsap.from(".api-header", {
          opacity: 0,
          x: -40,
          duration: 1,
          ease: "power2.out",
          scrollTrigger: {
            trigger: ".api-header",
            start: "top 85%",
            once: true,
          },
        });

        gsap.from(".api-header-desc", {
          opacity: 0,
          x: -40,
          duration: 1,
          ease: "power2.out",
          scrollTrigger: {
            trigger: ".api-header-desc",
            start: "top 85%",
            once: true,
          },
        });

        // Setiap fitur baris (icon + teks)
        const features = gsap.utils.toArray(".api-feature");
        features.forEach((feature, i) => {
          gsap.from(feature, {
            opacity: 0,
            x: -40,
            duration: 0.8,
            delay: i * 0.1,
            ease: "power2.out",
            scrollTrigger: {
              trigger: feature,
              start: "top 90%",
              once: true,
            },
          });
        });

        // Kode blok animasi masuk
        gsap.from(".api-codeblock", {
          opacity: 0,
          x: 80,
          duration: 1,
          ease: "power2.out",
          scrollTrigger: {
            trigger: ".api-codeblock",
            start: "top 85%",
            once: true,
          },
        });

      } catch (err) {
        console.error("API Showcase GSAP Error:", err);
      }
    };

    setTimeout(run, 150); // delay sedikit biar DOM ready
  }, []);

  return null;
}
