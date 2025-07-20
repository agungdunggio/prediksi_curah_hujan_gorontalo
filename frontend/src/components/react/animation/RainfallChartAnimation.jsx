import { useEffect } from "react";
import gsap from "gsap";
import { ScrollTrigger } from "gsap/ScrollTrigger";

export default function RainfallChartAnimation() {
  useEffect(() => {
    gsap.registerPlugin(ScrollTrigger);

    const runAnimation = () => {
      const title = document.querySelector(".rainfall-title");
      const subtitle = document.querySelector(".rainfall-subtitle");
      const chartContainer = document.querySelector(".rainfall-chart-container");

      if (!title || !subtitle || !chartContainer) {
        console.warn("⚠️ Elemen untuk animasi chart belum siap.");
        return;
      }

      const tl = gsap.timeline({
        scrollTrigger: {
          trigger: "#last-day-data",
          start: "top 75%",
          once: true,
        },
      });

      tl.fromTo(
        title,
        { opacity: 0, y: 30 },
        {
          opacity: 1,
          y: 0,
          duration: 1,
          ease: "power3.out",
        }
      );

      tl.fromTo(
        subtitle,
        { opacity: 0, y: 20 },
        {
          opacity: 1,
          y: 0,
          duration: 0.8,
          ease: "power2.out",
        },
        "-=0.7"
      );

      tl.fromTo(
        chartContainer,
        { opacity: 0, y: 20 },
        {
          opacity: 1,
          y: 0,
          duration: 1.2,
          ease: "power3.out",
        },
        "-=0.6"
      );
    };

    setTimeout(runAnimation, 100);
    
  }, []);

  return null;
}