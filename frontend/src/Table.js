import React from 'react';

const TableComponent = ({ data }) => {
  return (
    <table>
      <thead>
        <tr>
          <th> Headline </th>
          <th> Summary </th>
        </tr>
      </thead>
      <tbody>
        {data.map((article, index) => (
          <tr key={index}>
            <td>
              <a href={article.url} target="_blank" rel="noopener noreferrer">
                {article.title}
              </a>
            </td>
            <td>{article.summary}</td>
          </tr>
        ))}
      </tbody>
    </table>
  );
};

export default TableComponent;