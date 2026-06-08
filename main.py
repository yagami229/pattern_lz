import asyncio, a_fabric, legkoves, strategy

def main():
    asyncio.run(a_fabric.main())
    asyncio.run(legkoves.main())
    asyncio.run(strategy.main())


if __name__ == "__main__":
    main()