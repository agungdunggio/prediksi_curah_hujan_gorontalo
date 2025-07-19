import React from 'react';
import { Column } from '@ant-design/plots';
import { useBufferChartData } from '../../../hooks/useBufferChartData.ts';

const ColumnChartSection = () => {
  const { data, lastUpdate, loading } = useBufferChartData();

  const config = {
    data,
    xField: 'tanggal',
    yField: 'value',
    color: '#3b82f6',
    columnWidthRatio: 0.6,
    label: {
      position: 'middle',
      style: { fill: '#fff', fontSize: 12, fontWeight: 600 },
    },
    xAxis: {
      label: {
        autoHide: true,
        autoRotate: false,
        style: { fill: '#ccc', fontSize: 11 },
      },
    },
    yAxis: {
      label: {
        style: { fontSize: 12, fill: '#ccc' },
      },
    },
    tooltip: { showMarkers: false },
    interactions: [{ type: 'active-region' }],
  };

  return (
    <>
      <div className="text-white text-lg font-semibold mb-2">
        Statistik 15 Hari Terakhir
      </div>
      <div className="text-gray-400 text-sm mb-4">
        Terakhir diperbarui: {loading ? 'Memuat...' : lastUpdate || '-'}
      </div>
      <div className="bg-[#18181b] rounded-xl p-4 h-full">
        {!loading ? <Column {...config} /> : <div className="text-gray-500">Memuat grafik...</div>}
      </div>
    </>
  );
};

export default ColumnChartSection;
