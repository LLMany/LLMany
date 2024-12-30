import ModelElement from "./ModelElement";

function ModelList() {




    return (
        <div style={{
            display: 'flex',
            flexDirection: 'column',
            fontWeight: 'bold',
            gap: '4px',
        }}>
            Models
            <ModelElement
                modelName='ChatGPT'
                selected='true'
            />
            <ModelElement modelName='Gemini'/>
            <ModelElement modelName='Claude'/>
        </div>
    )
}

export default ModelList;