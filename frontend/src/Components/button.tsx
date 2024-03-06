export default function Button(props: {func: ()=>void, text: string}) {
    return (
        <button type="button" onClick={props.func}>
            {props.text}
        </button>
    )
}