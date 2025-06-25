import { useEffect } from "react";
import gsap from "gsap";
import { ScrollTrigger } from "gsap/ScrollTrigger";

export default function FeatureAnimation() {
  useEffect(() => {
    const initGSAP = async () => {
      try {
        gsap.registerPlugin(ScrollTrigger);

        // Header animation
        gsap.from(".feature-header", {
          opacity: 0,
          y: 60,
          duration: 1.2,
          ease: "power2.out",
          scrollTrigger: {
            trigger: ".feature-header",
            once: true,
            start: "top 85%",
            toggleActions: "play none none reverse",
          },
        });

        // Animasi tiap kartu secara individu
        const cards = gsap.utils.toArray(".feature-card");
        if (!cards.length) return;

        cards.forEach((card, i) => {
          gsap.from(card, {
            opacity: 0,
            y: 80,
            scale: 0.9,
            duration: 1,
            delay: i * 0.2, 
            ease: "back.out(1.7)",
            scrollTrigger: {
              trigger: card,
              once: true, 
              start: "top 85%",
              toggleActions: "play none none reverse",
            },
          });

          // Hover effect
          card.addEventListener("mouseenter", () => {
            gsap.to(card, { y: -10, scale: 1.02, duration: 0.3 });
          });
          card.addEventListener("mouseleave", () => {
            gsap.to(card, { y: 0, scale: 1, duration: 0.3 });
          });
        });

      } catch (error) {
        console.error("GSAP Error:", error);
      }
    };

    setTimeout(initGSAP, 150); 
  }, []);

  return null;
}
