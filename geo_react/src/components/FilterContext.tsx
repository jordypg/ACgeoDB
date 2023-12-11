// FilterContext.tsx
import React, { createContext, useContext, useState, ReactNode } from 'react';

interface FilterContextProps {
  filterValue: string;
  setFilterValue: React.Dispatch<React.SetStateAction<string>>;
}

const FilterContext = createContext<FilterContextProps | undefined>(undefined);

export const FilterProvider: React.FC<{children: ReactNode }> = ({ children }) => {
  const [filterValue, setFilterValue] = useState('');

  return (
    <FilterContext.Provider value={{ filterValue, setFilterValue }}>
      {children}
    </FilterContext.Provider>
  );
};

export const useFilterContext = () => {
  const context = useContext(FilterContext);
  if (!context) {
    throw new Error('useFilterContext must be used within a FilterProvider');
  }
  return context;
};
