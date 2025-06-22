// Global VANTA object from CDN
declare global {
    interface Window {
        VANTA: {
            NET: (config: VantaNetConfig) => any;
        };
    }
}

interface VantaNetConfig {
    el: string | HTMLElement;
    THREE?: any;
    mouseControls?: boolean;
    touchControls?: boolean;
    gyroControls?: boolean;
    minHeight?: number;
    minWidth?: number;
    scale?: number;
    scaleMobile?: number;
    color?: number;
    backgroundColor?: number;
    points?: number;
    maxDistance?: number;
    spacing?: number;
}

// Legacy module declaration for direct imports
declare module 'vanta/dist/vanta.net.min.js' {
    function NET(config: VantaNetConfig): any;
    export default NET;
}

export {}; 