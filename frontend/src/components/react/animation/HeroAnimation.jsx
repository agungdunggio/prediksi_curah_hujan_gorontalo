import { useEffect } from "react";
import gsap from "gsap";

export default function HeroAnimation() {
  useEffect(() => {
    const run = () => {
      const title = document.querySelector(".hero-title");
      const desc = document.querySelector(".hero-desc");
      const buttons = document.querySelectorAll(".hero-buttons a");

      if (!title || !desc || buttons.length === 0) {
        console.warn("❌ Hero elements not ready.");
        return;
      }

      const tl = gsap.timeline();

      // TITLE
      tl.fromTo(
        title,
        { opacity: 0, y: 40 },
        {
          opacity: 1,
          y: 0,
          duration: 0.8,
          ease: "power3.out",
        }
      );

      // DESCRIPTION
      tl.fromTo(
        desc,
        { opacity: 0, y: 30 },
        {
          opacity: 1,
          y: 0,
          duration: 0.6,
          ease: "power2.out",
        },
        "-=0.5"
      );

      // BUTTONS (now each button has its own opacity-0 + translate-y-10)
      tl.fromTo(
        buttons,
        { opacity: 0, y: 10 },
        {
          opacity: 1,
          y: 0,
          duration: 0.2,
          ease: "power3.out",
        },
        "-=0.4"
      );
    };

    setTimeout(run, 100); // wait a bit to ensure DOM is ready
  }, []);

  return null;
}
