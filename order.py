import re
import argparse

def order_citations(text):
    # Find all citations in the format [x, y, z]
    citations = re.findall(r'\[(.*?)\]', text)
    print("citations: ", citations)
    
    # Function to sort numbers within each citation
    def sort_citation(citation):
        numbers = list(map(int, citation.split(',')))
        numbers.sort()
        return '[' + ', '.join(map(str, numbers)) + ']'
    
    # Replace each citation in the text with the sorted citation
    for citation in citations:
        numbers = citation.split(',')
        if len(numbers) > 2:
            sorted_citation = sort_citation(citation)
            text = text.replace(f'[{citation}]', sorted_citation)
    
    return text

def main():
    # Set up argument parsing
    parser = argparse.ArgumentParser(description='Order citations in a paper.')
    parser.add_argument('source', type=str, help='Path to the source paper file.')
    parser.add_argument('target', type=str, help='Path to the target paper file.')
    args = parser.parse_args()
    
    # Read the input file
    with open(args.source, 'r') as file:
        content = file.read()
    
    # Order the citations
    ordered_content = order_citations(content)
    
    # Write the ordered content to the new file
    with open(args.target, 'w') as file:
        file.write(ordered_content)

if __name__ == "__main__":
    main()