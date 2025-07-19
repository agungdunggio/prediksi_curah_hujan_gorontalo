import { Pie } from '@ant-design/plots';
import React, { useEffect, useRef } from 'react';
import gsap from 'gsap';
import { ScrollTrigger } from 'gsap/ScrollTrigger';

const PieChartDataSet = () => {
  const chartRef = useRef(null);

  const data = [
    { type: 'Data Train', value: 70 },
    { type: 'Data Test', value: 30 },
  ];

  const config = {
    data,
    angleField: 'value',
    colorField: 'type',
    radius: 0.85,
    label: {
      type: 'spider',
      content: '{type}\n{value}%',
      style: { fontWeight: 'bold', fontSize: 20, fill: '#222' },
    },
    legend: false,
    tooltip: { title: 'type' },
    animation: {
      appear: {
        animation: 'wave-in',
        duration: 1200,
        easing: 'easeCubicOut',
      },
    },
    interaction: {
      elementHighlight: true,
      tooltip: true,
    },
    state: { inactive: { opacity: 0.5 } },
  };

  useEffect(() => {
    gsap.registerPlugin(ScrollTrigger);
    gsap.fromTo(
      chartRef.current,
      { opacity: 0, scale: 0.8 },
      {
        opacity: 1,
        scale: 1,
        duration: 1.1,
        ease: 'power2.out',
        scrollTrigger: {
          trigger: chartRef.current,
          start: 'top 85%',
          once: true,
        },
      }
    );
  }, []);

  return (
    <div
      ref={chartRef}
      style={{
        width: '100%',
        maxWidth: 400,
        margin: '0 auto',
        background: 'rgba(30,30,40,0.9)',
        borderRadius: 24,
        boxShadow: '0 8px 32px rgba(0,0,0,0.25)',
        padding: 24,
      }}
    >
      <Pie {...config} />
    </div>
  );
};

export default PieChartDataSet;