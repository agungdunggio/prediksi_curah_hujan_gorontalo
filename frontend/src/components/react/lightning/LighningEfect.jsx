import * as THREE from 'three';
import React, { useRef, useEffect } from 'react';

const LightingEffect = ({
  position = [0, 5, 0],
  color = '#FF0000',
  rotation = [0, 0, 0], // agar bisa disesuaikan arah cahaya
  coneSize = [5, 8], // [radius, height]
  opacity = 0.2
}) => {
  const targetRef = useRef(new THREE.Object3D());
  const lightRef = useRef();

  useEffect(() => {
    targetRef.current.position.set(position[0], 0, position[2]);
    if (lightRef.current) {
      lightRef.current.target = targetRef.current;
    }
  }, [position]);

  return (
    <>
      <primitive object={targetRef.current} />

      <spotLight
        ref={lightRef}
        position={position}
        angle={Math.PI / 2.5} // lebih lebar
        distance={30}
        intensity={1.2}
        penumbra={1}
        color={color}
        castShadow
      />

      <mesh
        position={[position[0], position[1] - coneSize[1] / 2, position[2]]}
        rotation={rotation}
      >
        <coneGeometry args={[coneSize[0], coneSize[1], 32, 1, true]} />
        <meshBasicMaterial
          color={color}
          opacity={opacity}
          transparent
          side={THREE.DoubleSide}
        />
      </mesh>
    </>
  );
};

export default LightingEffect;
