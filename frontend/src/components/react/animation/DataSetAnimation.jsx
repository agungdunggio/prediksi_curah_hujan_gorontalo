import { useEffect } from "react";
import gsap from "gsap";
import { ScrollTrigger } from "gsap/ScrollTrigger";

export default function DataSetAnimation() {
  useEffect(() => {
    gsap.registerPlugin(ScrollTrigger);

    gsap.from(".dataset-text", {
      opacity: 0,
      x: 50,
      duration: 1,
      delay: 0.3,
      ease: "power2.out",
      scrollTrigger: {
        trigger: ".dataset-text",
        start: "top 85%",
        once: true,
      },
    });
  }, []);

  return null; // Karena hanya untuk efek animasi
}
