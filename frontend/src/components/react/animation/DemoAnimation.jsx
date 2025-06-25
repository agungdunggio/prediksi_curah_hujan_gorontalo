import { useEffect } from "react";
import gsap from "gsap";
import { ScrollTrigger } from "gsap/ScrollTrigger";

export default function DemoAnimation() {
  useEffect(() => {
    const run = async () => {
      try {
        gsap.registerPlugin(ScrollTrigger);

        gsap.from(".demo-header", {
            opacity: 0,
            y: 60,
            duration: 1,
            ease: "power2.out",
            scrollTrigger: {
                trigger: ".demo-header",
                start: "top 85%",
                once: true,
            },
        });

        gsap.from(".demo-form", {
            opacity: 0,
            y: 40,
            duration: 1,
            delay: 0.5,
            ease: "power2.out",
            scrollTrigger: {
                trigger: ".demo-form",
                start: "top 85%",
                once: true,
            },
        });

        gsap.from(".demo-result", {
            opacity: 0,
            y: 40,
            duration: 1,
            delay: 0.7,
            ease: "power2.out",
            scrollTrigger: {
                trigger: ".demo-result",
                start: "top 85%",
                once: true,
            },
        });


      } catch (error) {
        console.error("Error loading GSAP:", error);
      }
    };
    run();
  }, []);
}