import { useEffect } from "react";
import gsap from "gsap";

export default function HeroAnimation() {
  useEffect(() => {
    const ctx = gsap.context(() => {
      const title = document.querySelector(".hero-title");
      const desc = document.querySelector(".hero-desc");
      const buttons = gsap.utils.toArray(".hero-buttons a");
      if (!title || !desc || buttons.length === 0) return;
  
      const tl = gsap.timeline();
      tl.fromTo(
        title,
        { opacity: 0, y: 40 },
        { opacity: 1, y: 0, duration: 0.8, ease: "power3.out" }
      )
        .fromTo(
          desc,
          { opacity: 0, y: 30 },
          { opacity: 1, y: 0, duration: 0.6, ease: "power2.out" },
          "-=0.5"
        )
        .fromTo(
          buttons,
          { opacity: 0, y: 10 },
          {
            opacity: 1,
            y: 0,
            duration: 0.4,
            ease: "power3.out",
            stagger: { each: 0.15, from: "start" },
            overwrite: "auto",               
          },
          "-=0.4"
        );
    });

    return () => ctx.revert();
  }, []);
  

  return null;
}
