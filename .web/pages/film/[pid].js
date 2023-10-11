import { Fragment, useContext, useEffect, useRef, useState } from "react"
import { useRouter } from "next/router"
import { Event, getAllLocalStorageItems, getRefValue, getRefValues, isTrue, preventDefault, refs, spreadArraysOrObjects, uploadFiles, useEventLoop } from "/utils/state"
import { EventLoopContext, initialEvents, StateContext } from "/utils/context.js"
import "focus-visible/dist/focus-visible"
import { Avatar, Box, Button, Divider, Grid, GridItem, HStack, Image, Link, Modal, ModalBody, ModalContent, ModalHeader, ModalOverlay, option, Select, Text, useColorMode, VStack } from "@chakra-ui/react"
import NextLink from "next/link"
import { StarIcon } from "@chakra-ui/icons"
import NextHead from "next/head"



export default function Component() {
  const state = useContext(StateContext)
  const router = useRouter()
  const { colorMode, toggleColorMode } = useColorMode()
  const focusRef = useRef();
  
  // Main event loop.
  const [addEvents, connectError] = useContext(EventLoopContext)

  // Set focus to the specified element.
  useEffect(() => {
    if (focusRef.current) {
      focusRef.current.focus();
    }
  })

  // Route after the initial page hydration.
  useEffect(() => {
    const change_complete = () => addEvents(initialEvents.map((e) => ({...e})))
    router.events.on('routeChangeComplete', change_complete)
    return () => {
      router.events.off('routeChangeComplete', change_complete)
    }
  }, [router])


  return (
    <Fragment>
  <Fragment>
  {isTrue(connectError !== null) ? (
  <Fragment>
  <Modal isOpen={connectError !== null}>
  <ModalOverlay>
  <ModalContent>
  <ModalHeader>
  {`Connection Error`}
</ModalHeader>
  <ModalBody>
  <Text>
  {`Cannot connect to server: `}
  {(connectError !== null) ? connectError.message : ''}
  {`. Check if server is reachable at `}
  {`http://localhost:8000`}
</Text>
</ModalBody>
</ModalContent>
</ModalOverlay>
</Modal>
</Fragment>
) : (
  <Fragment/>
)}
</Fragment>
  <Box sx={{"width": "100%", "maxWidth": "960px", "bg": "white", "h": "100%", "px": [4, 12], "margin": "10px auto", "position": "relative"}}>
  <Link as={NextLink} href={`/`}>
  <Image src={`/logo.png`} sx={{"width": "auto", "height": "30px", "position": "absolute", "top": "0px", "left": "0px"}}/>
</Link>
  <Fragment>
  {isTrue(state.user_login) ? (
  <Fragment>
  <Link as={NextLink} href={`/profile`} sx={{"position": "absolute", "top": "0px", "right": "0px"}}>
  <Avatar size={`xs`}/>
</Link>
</Fragment>
) : (
  <Fragment>
  <Link as={NextLink} href={`/login`} sx={{"position": "absolute", "top": "0px", "right": "0px"}}>
  <Button size={`xs`}>
  {`Login / Sign up`}
</Button>
</Link>
</Fragment>
)}
</Fragment>
  <VStack>
  <Text>
  {state.film_state.title}
</Text>
  <Divider sx={{"borderColor": "black"}}/>
  <Grid sx={{"width": "100%", "gap": 4}} templateColumns={`repeat(6, 1fr)`} templateRows={`repeat(4, 1fr)`}>
  <GridItem colSpan={1} rowSpan={2}>
  <VStack>
  <Text sx={{"font-family": "Helvetica, sans-serif", "font-size": "10px", "padding": "1px", "font-weight": "bold", "align-self": "flex-start"}}>
  {`Title`}
</Text>
  <Text sx={{"font-family": "Helvetica, sans-serif", "font-size": "10px", "padding": "1px", "font-weight": "bold", "align-self": "flex-start"}}>
  {`Year`}
</Text>
  <Text sx={{"font-family": "Helvetica, sans-serif", "font-size": "10px", "padding": "1px", "font-weight": "bold", "align-self": "flex-start"}}>
  {`Genres`}
</Text>
  <Text sx={{"font-family": "Helvetica, sans-serif", "font-size": "10px", "padding": "1px", "font-weight": "bold", "align-self": "flex-start"}}>
  {`Run time`}
</Text>
  <Text sx={{"font-family": "Helvetica, sans-serif", "font-size": "10px", "padding": "1px", "font-weight": "bold", "align-self": "flex-start"}}>
  {`Num Votes`}
</Text>
</VStack>
</GridItem>
  <GridItem colSpan={3} rowSpan={4}>
  <VStack>
  <Text sx={{"font-family": "Helvetica, sans-serif", "font-size": "10px", "padding": "1px", "align-self": "flex-start"}}>
  {state.film_state.title}
</Text>
  <Text sx={{"font-family": "Helvetica, sans-serif", "font-size": "10px", "padding": "1px", "align-self": "flex-start"}}>
  {state.film_state.year}
</Text>
  <Text sx={{"font-family": "Helvetica, sans-serif", "font-size": "10px", "padding": "1px", "align-self": "flex-start"}}>
  {state.film_state.genres}
</Text>
  <Text sx={{"font-family": "Helvetica, sans-serif", "font-size": "10px", "padding": "1px", "align-self": "flex-start"}}>
  {state.film_state.runtime}
</Text>
  <Text sx={{"font-family": "Helvetica, sans-serif", "font-size": "10px", "padding": "1px", "align-self": "flex-start"}}>
  {state.film_state.numVotes}
</Text>
</VStack>
</GridItem>
  <GridItem colSpan={1} colStart={-1} rowSpan={1}>
  <VStack>
  <Text sx={{"font-family": "Helvetica, sans-serif", "font-size": "10px", "font-weight": "bold"}}>
  {`Avg Rating`}
</Text>
  <HStack>
  <StarIcon/>
  <Text>
  {state.film_state.averageRating}
</Text>
</HStack>
  <Text sx={{"font-family": "Helvetica, sans-serif", "font-size": "10px", "font-weight": "bold"}}>
  {`Your rate`}
</Text>
  <Fragment>
  {isTrue(state.user_login) ? (
  <Fragment>
  <Select onChange={(_e0) => addEvents([Event("state.film_state.rate_film", {rate:_e0.target.value})], (_e0))} placeholder={`Rate film`} size={`xs`} sx={{"colorSchemes": "twitter"}}>
  {state.film_state.rate_options.map((wmmljoty, i) => (
  <option key={i} value={wmmljoty}>
  {wmmljoty}
</option>
))}
</Select>
</Fragment>
) : (
  <Fragment>
  <Text sx={{"font-family": "Helvetica, sans-serif", "font-size": "8px", "font-weight": "bold"}}>
  {`Login to rate.`}
</Text>
</Fragment>
)}
</Fragment>
</VStack>
</GridItem>
</Grid>
</VStack>
</Box>
  <NextHead>
  <title>
  {`Reflex App`}
</title>
  <meta content={`A Reflex app.`} name={`description`}/>
  <meta content={`favicon.ico`} property={`og:image`}/>
</NextHead>
</Fragment>
  )
}
