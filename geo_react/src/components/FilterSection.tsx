// FilterSection.tsx
import styled from 'styled-components';
import SearchFilter from './SearchFilter';
import { FilterProvider } from './FilterContext';


const FilterContainer = styled.div`
  padding: 20px;
  border-right: 1px solid #ccc;
`;


const FilterSection: React.FC = () => {
  return (
    <FilterProvider>
      <FilterContainer>
        <h2>Filters</h2>
        <SearchFilter/>
        {/* Add more filters as needed */}
      </FilterContainer>
    </FilterProvider>
  );
};

export default FilterSection;
