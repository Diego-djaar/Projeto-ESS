// CpfContext.tsx
import React, { createContext, useState, useContext, ReactNode } from 'react';

type CpfContextType = [string, React.Dispatch<React.SetStateAction<string>>];

const CpfContext = createContext<CpfContextType | undefined>(undefined);

export const useCpf = () => {
  const context = useContext(CpfContext);
  if (context === undefined) {
    throw new Error('useCpf must be used within a CpfProvider');
  }
  return context;
};

interface CpfProviderProps {
  children: ReactNode; // Esta é a tipagem correta para 'children'
}

export const CpfProvider: React.FC<CpfProviderProps> = ({ children }) => {
  const [cpf, setCpf] = useState<string>(''); // O estado é tipado explicitamente como string
  return (
    <CpfContext.Provider value={[cpf, setCpf]}>
      {children}
    </CpfContext.Provider>
  );
};
