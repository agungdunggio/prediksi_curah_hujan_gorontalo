export type BufferDataItem = {
    date: string;
    value: number;
  };
  
  export type BufferStatusResponse = {
    status: boolean;
    message: string;
    data: {
      current_size: number;
      needed: number;
      current_data: BufferDataItem[];
      updated_at: string | null;
    };
  };
  
  export type ChartDataItem = {
    tanggal: string;
    value: number;
  };
  