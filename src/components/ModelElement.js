function ModelElement({ modelName, selected }) {

    return (
        <div style={{
            flex: 1,
            borderRadius: '8px',
            padding: '2px',
            background: selected ? '#666666' : '#444444',
            color: 'white',
        }}>
            {modelName}
        </div>
    )
}

export default ModelElement;