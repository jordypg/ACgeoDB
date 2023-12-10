// FilterSection.tsx
import React, { useState } from 'react';
import styled from 'styled-components';
import SearchFilter from './SearchFilter';

const FilterContainer = styled.div`
  padding: 20px;
  border-right: 1px solid #ccc;
`;

const FilterSection: React.FC = () => {
  const [searchQuery, setSearchQuery] = useState('');

  const handleSearch = (query: string) => {
    setSearchQuery(query);
    console.log('3')
    console.log(searchQuery)
    console.log(query)
    // Perform any additional logic here, such as updating a list of filtered items.
    // You might want to use the query to filter your data and update the displayed items accordingly.
  };

  return (
    <FilterContainer>
      <h2>Filters</h2>
      <SearchFilter onSearch={handleSearch} />
      {/* Add more filters as needed */}
    </FilterContainer>
  );
};

export default FilterSection;
