// FilterSection.tsx
import styled from 'styled-components';
import SearchFilter from './SearchFilter';


const FilterContainer = styled.div`
  padding: 20px;
  border-right: 1px solid #ccc;
`;


const FilterSection: React.FC = () => {
  return (
      <FilterContainer>
        <h2>Filters</h2>
        <SearchFilter/>
        {/* Add more filters as needed */}
      </FilterContainer>
  );
};

export default FilterSection;
